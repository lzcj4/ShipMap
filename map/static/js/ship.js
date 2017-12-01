var SHIP_IDENTIFY_DISTANCE = 50;

var currentCircle;
var circleList = [];
var radarShipDict = new RadarShipsDict();

function addShip(radar, pos) {
    var ship = new AMap.Marker({
        draggable: true,
        position: pos,
    });
    ship.setMap(map);
    ship.on('click', function () {
        infoWindow.open(map, ship.getPosition());
    });

    // AMap.event.addListener(ship, 'click', function () {
    //     infoWindow.open(map, ship.getPosition());
    // });
    setShipIcon(ship);
    radarShipDict.put(radar, ship);
}

function setShipIcon(ship) {
    if (checkElementIsNone(ship)) {
        return;
    }

    var isInArea = checkPositionInArea(ship.getPosition());
    ship.setTitle(isInArea ? "已方船只" : "未知船只");
    ship.setIcon(isInArea ? "http://oyjbgqiy4.bkt.clouddn.com/ship.png" : "http://oyjbgqiy4.bkt.clouddn.com/blackship.png");
}

function getShip(lnglat) {
    var result = null;
    var allShip = radarShipDict.items();
    for (var i in allShip) {
        var ship = allShip[i];
        var distance = ship.getPosition().distance(lnglat);
        console.log("get ship distance:" + distance);
        if (distance <= SHIP_IDENTIFY_DISTANCE) {
            result = ship;
            break;
        }
    }
    return result;
}

function addShipByRadar(radarItems) {
    if (radarItems == null) {
        return;
    }

    var radarName = radarItems.radar;
    var items = radarItems.items;
    clearShips(radarShipDict.get(radarName));
    for (var i in items) {
        var lnglat = items[i];
        var pos = new AMap.LngLat(lnglat.longitude, lnglat.latitude);
        var lngDist = Math.cos(lnglat.direction / 180) * lnglat.distance;
        var latDist = Math.sin(lnglat.direction / 180) * lnglat.distance;
        var newPos = pos.offset(lngDist, latDist);
        var ship = getShip(radarName, newPos);
        if (ship == null) {
            addShip(newPos);
        } else {
            ship.setPosition(newPos);
        }
    }
    checkAllShipInArea();
}

function setRadiusChange(newRadius) {
    try {
        var r = parseFloat(newRadius);
        if (!checkElementIsNone(currentCircle)) {
            if (r != currentCircle.getRadius()) {
                currentCircle.setRadius(r);
                checkAllShipInArea();
            }
        }
    } catch (ex) {
    }
}

function checkPositionInArea(pos) {
    var result = false;
    for (var index in circleList) {
        var c = circleList[index];
        if (c.contains(pos)) {
            result = true;
            break;
        }
    }
    return result;
}

function checkAllShipInArea() {
    var allShip = radarShipDict.items();
    for (var index in allShip) {
        var ship = allShip[index];
        setShipIcon(ship)
    }
}

// function clearShips() {
//     radarShipDict.clear();
//     map.remove(shipList);
//     shipList.length = 0;
// }

function clearShips(ships) {
    if (ships == null || ships.length == 0) {
        return;
    }
    map.remove(ships);
    ships.length = 0;
}

function addCircle(pos, radius, id) {
    var circle = new AMap.Circle({
        bubble: false,
        map: map,
        center: pos, //设置线覆盖物路径
        radius: radius, //米
        strokeColor: "#3366FF", //边框线颜色
        strokeOpacity: 0.3, //边框线透明度
        strokeWeight: 3, //边框线宽
        fillColor: "#FFA500", //填充色
        fillOpacity: 0.35,//填充透明度
    });

    var extData = {};
    if (!checkElementIsNone(id)) {
        extData['id'] = id;
    }
    else {
        extData['id'] = new Date().getTime().toString();
    }
    circleList.push(circle);
    circle.setExtData(extData);
    // http: //lbs.amap.com/api/javascript-api/reference/plugin#AMap.CircleEditor
    circle.on('dblclick', function (e) {
        map.plugin(["AMap.CircleEditor"], function (e) {
            currentCircle = circle;
            var ce = new AMap.CircleEditor(map, circle);
            var extData = circle.getExtData();
            extData['editor'] = ce;
            circle.setExtData(extData);
            ce.open();
        });
    });

    circle.on('rightclick', function (e) {
        currentCircle = null;
        var extData = circle.getExtData()
        if (extData.editor) {
            extData.editor.close();
            var json = {
                'id': extData.id,
                "lnglat": [circle.getCenter().getLng(), circle.getCenter().getLat()],
                "radius": circle.getRadius()
            };
            wsSend(WS_CMD.area, "", JSON.stringify(json));
        }
    });

    circle.on('change', function (e) {
        checkAllShipInArea();
        $("#txtRadius").val(circle.getRadius());
    });
    return circle;
}

var title = '哈哈<span style="font-size:11px;color:#F00;">小三贼船</span>';
var content = [];
content.push("<img src='http://tpc.googlesyndication.com/simgad/5843493769827749134'>地址：北京市朝阳区阜通东大街6号院3号楼东北8.3公里");
content.push("电话：010-64733333");
content.push("<a href='http://ditu.amap.com/detail/B000A8URXB?citycode=110105'>详细信息</a>");
var infoWindow = new AMap.InfoWindow({
    isCustom: true, //使用自定义窗体
    content: createInfoWindow(title, content.join("<br/>")),
    offset: new AMap.Pixel(16, -45)
});

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

//关闭信息窗体
function closeInfoWindow() {
    map.clearInfoWindow();
}
