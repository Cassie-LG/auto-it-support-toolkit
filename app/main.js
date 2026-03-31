const { app, BrowserWindow, Tray, Menu } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let mainWindow;
let tray;
let flaskProcess;

// Create the main Electron window
function createWindow() {
    mainWindow = new BrowserWindow({
        width: 900,
        height: 600,
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true
        },
        icon: path.join(__dirname, 'icon.png')
    });

    mainWindow.loadURL('http://127.0.0.1:5000');

    mainWindow.on('closed', function () {
        mainWindow = null;
    });
}

// Start Flask server
function startFlask() {
    // Windows vs Unix commands
    const python = process.platform === 'win32' ? 'python' : 'python3';
    // Start continuous monitoring system
    flaskProcess = spawn(python, ['main.py'], {
        cwd: path.join(__dirname, '..')
    });

    // Start Flask dashboard separately
    const flaskDashboard = spawn(python, ['dashboard.py'], {
        cwd: path.join(__dirname, '..')
    });

    flaskProcess.stdout.on('data', (data) => {
        console.log(`Dashboard: ${data}`);
    });

    flaskProcess.stderr.on('data', (data) => {
        console.error(`Dashboard error: ${data}`);
    });
}

// Tray Menu
function createTray() {
    tray = new Tray(path.join(__dirname, 'icon.png'));
    const contextMenu = Menu.buildFromTemplate([
        { label: 'Show App', click: () => mainWindow.show() },
        { label: 'Quit', click: () => app.quit() }
    ]);
    tray.setToolTip('Auto IT Support Toolkit');
    tray.setContextMenu(contextMenu);
}

app.on('ready', () => {
    startFlask();
    createWindow();
    createTray();
});

app.on('window-all-closed', () => {
    // Keep app running in tray
    if (process.platform !== 'darwin') {
        // Do not quit app; handled via tray
    }
});

app.on('activate', () => {
    if (mainWindow === null) createWindow();
});

app.on('quit', () => {
    if (flaskProcess) flaskProcess.kill();
});