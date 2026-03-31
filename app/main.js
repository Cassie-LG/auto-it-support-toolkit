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

    // Wait for Flask to start
    setTimeout(() => {
        mainWindow.loadURL('http://127.0.0.1:5000');
    }, 3000);

    mainWindow.on('closed', function () {
        mainWindow = null;
    });
}

// Start Flask server
function startFlask() {
    const isDev = !app.isPackaged;
    const basePath = isDev ? path.join(__dirname, '..') : path.join(process.resourcesPath, 'app');
    const python = 'python';

    //Start main monitoring
    flaskProcess = spawn(python, ['main.py'], {
        cwd: basePath
    });

    //Start dashboard
    const dashboardProcess = spawn(python, ['dashboard.py'], {
        cwd: basePath
    });

    flaskProcess.stdout.on('data', (data) => {
        console.log(`Main: ${data}`);
    });

    flaskProcess.stderr.on('data', (data) => {
        console.error(`Main error: ${data}`);
    });

    dashboardProcess.stdout.on('data', (data) => {
        console.log(`Dashboard: ${data}`);
    });

    dashboardProcess.stderr.on('data', (data) => {
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