function checkElementIsNone(element) {
    var isNone = element === undefined || element === null;
    return isNone;
}

function checkElementNoneById(eleId) {
    return checkElementIsNone($(eleId));
}


function Dictionary() {
    var items = {};

    this.has = function (key) {
        return key in items;
    };

    this.put = function (key, value) {
        items[key] = value;
    };

    this.remove = function (key) {
        if (this.has(key)) {
            delete items[key];
            return true;
        }
        return false;
    };

    this.get = function (key) {
        var result = this.has(key) ? items[key] : null;
        return result;
    };

    this.values = function () {
        var values = [];
        for (var k in items) {
            if (this.has(k)) {
                values.push(items[k]);
            }
        }
        return values;
    };

    this.clear = function () {
        items = {};
    };

    this.size = function () {
        var count = 0;
        for (var prop in items) {
            if (items.hasOwnProperty(prop)) {
                ++count;
            }
        }
        return count;
    };

    this.getItems = function () {
        return items;
    };
}


function RadarShipsDict() {
    var radarDict = new Dictionary();

    this.get = function (radarName) {
        return radarDict.get(radarName);
    };

    this.put = function (radarName, ship) {
        var items = radarDict.get(radarName);
        if (items == null) {
            items = [ship];
            radarDict.put(radarName, items);
        } else {
            items.push(ship);
        }
    };

    this.items = function () {
        var result = [];
        var items = radarDict.getItems();
        for (var k in items) {
            result = result.concat(items[k]);
        }
        return result;
    };

    this.clear = function () {
        var items = radarDict.getItems()
        for (var k in items) {
            clearShips(items[k])
        }
        radarDict.clear();
    };
}






