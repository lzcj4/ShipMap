var scale = new AMap.Scale({
    visible: false
});
var toolBar = new AMap.ToolBar({
    visible: false
});
var overView = new AMap.OverView({
    visible: false
});

map.addControl(scale);
map.addControl(toolBar);
map.addControl(overView);

function toggleScale(checkbox) {
    if (checkbox.checked) {
        scale.show();
    } else {
        scale.hide();
    }
}

function toggleToolBar(checkbox) {
    if (checkbox.checked) {
        showToolBar();
        showToolBarDirection();
        showToolBarRuler();
    } else {
        hideToolBar();
        hideToolBarDirection();
        hideToolBarRuler();
    }
}

function toggleToolBarDirection(checkbox) {
    if (checkbox.checked) {
        toolBar.showDirection()
    } else {
        toolBar.hideDirection()
    }
}

function toggleToolBarRuler(checkbox) {
    if (checkbox.checked) {
        toolBar.showRuler();
    } else {
        toolBar.hideRuler();
    }
}

function toggleOverViewShow(checkbox) {
    if (checkbox.checked) {
        overView.show();
        document.getElementById('overviewOpen').disabled = false;
    } else {
        overView.hide();
        document.getElementById('overviewOpen').disabled = true;
    }
}

function toggleOverViewOpen(checkbox) {
    if (checkbox.checked) {
        overView.open();
    }
    else {
        overView.close();
    }
}

function showToolBar() {
    document.getElementById('toolbar').checked = true;
    document.getElementById('toolbarDirection').disabled = false;
    document.getElementById('toolbarRuler').disabled = false;
    toolBar.show();
}

function hideToolBar() {
    document.getElementById('toolbar').checked = false;
    document.getElementById('toolbarDirection').disabled = true;
    document.getElementById('toolbarRuler').disabled = true;
    toolBar.hide();
}

function showToolBarDirection() {
    document.getElementById('toolbarDirection').checked = true;
    toolBar.showDirection();
}

function hideToolBarDirection() {
    document.getElementById('toolbarDirection').checked = false;
    toolBar.hideDirection();
}

function showToolBarRuler() {
    document.getElementById('toolbarRuler').checked = true;
    toolBar.showRuler();
}

function hideToolBarRuler() {
    document.getElementById('toolbarRuler').checked = false;
    toolBar.hideRuler();
}