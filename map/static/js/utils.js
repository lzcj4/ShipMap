function checkElementIsNone(element) {
    var isNone = element === undefined || element === null;
    return isNone;
}

function checkElementNoneById(eleId) {
    return checkElementIsNone($(eleId));
}
