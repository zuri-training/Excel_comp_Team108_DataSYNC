//gET the elements with class="column"

var elements = document.getElementsByClassName("column");

//Declare a Loop Variable
var i;

//List vIEW
function listView() {
    for (i = 0; i < elements.length; i++) {
        elements[i].style.width = "100%"
    }
}

// Grid View
function gridView() {
    for (i = 0; i < elements.length; i++) {
        elements[i].style.width = "20%"
    }

}
