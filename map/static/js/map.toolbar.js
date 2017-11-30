

    //构建自定义信息窗体
    function createInfoWindow(title, content) {
        var info = document.createElement("div");
        info.className = "info";

        //可以通过下面的方式修改自定义窗体的宽高
        //info.style.width = "400px";
        // 定义顶部标题
        var top = document.createElement("div");
        var titleD = document.createElement("div");
        var closeX = document.createElement("img");
        top.className = "info-top";
        titleD.innerHTML = title;
        closeX.src = "http://webapi.amap.com/images/close2.gif";
        closeX.onclick = closeInfoWindow;

        top.appendChild(titleD);
        top.appendChild(closeX);
        info.appendChild(top);

        // 定义中部内容
        var middle = document.createElement("div");
        middle.className = "info-middle";
        middle.style.backgroundColor = 'white';
        middle.innerHTML = content;
        info.appendChild(middle);

        // 定义底部内容
        var bottom = document.createElement("div");
        bottom.className = "info-bottom";
        bottom.style.position = 'relative';
        bottom.style.top = '0px';
        bottom.style.margin = '0 auto';
        var sharp = document.createElement("img");
        sharp.src = "http://webapi.amap.com/images/sharp.png";
        bottom.appendChild(sharp);
        info.appendChild(bottom);
        return info;
    }

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