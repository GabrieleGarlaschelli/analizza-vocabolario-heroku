function showWords() {
    var myTable = document.getElementById("Table");
    var checkBox = document.getElementById("blacklist");


    var dropdown = document.getElementById("wordselect");
    var dropdown_value = dropdown.options[dropdown.selectedIndex].value;

    if(checkBox.checked){
        if (dropdown_value == '1') {
            for(var i = 0; i < myTable.rows.length; i++) {
                myTable.rows[i].style.display = "";
                if (myTable.rows[i].cells[0].innerHTML.length < 2) {
                    myTable.rows[i].style.display = "none";
                }
            }
        } else if (dropdown_value == '2') {
            for(var i = 0; i < myTable.rows.length; i++) {
                if (myTable.rows[i].cells[0].innerHTML.length < 3) {
                    myTable.rows[i].style.display = "none";
                }
            }
        }else {
            for(var i = 0; i < myTable.rows.length; i++) {
                myTable.rows[i].style.display = "";
            }
        }
    }else{
        if (dropdown_value == '1') {
            for(var i = 0; i < myTable.rows.length; i++) {
                myTable.rows[i].style.display = "";
                if (myTable.rows[i].cells[0].innerHTML.length < 2) {
                    myTable.rows[i].style.display = "none";
                }else{
                    for(var j = 0; j < blacklist_list.length; j++){
                        if(myTable.rows[i].cells[0].innerHTML == blacklist_list[j] ){
                            myTable.rows[i].style.display = "none";
                        }
                    }
                }
            }
        } else if (dropdown_value == '2') {
            for(var i = 0; i < myTable.rows.length; i++) {
                myTable.rows[i].style.display = "";
                if (myTable.rows[i].cells[0].innerHTML.length < 3) {
                    myTable.rows[i].style.display = "none";
                }else{
                    for(var j = 0; j < blacklist_list.length; j++){
                        if(myTable.rows[i].cells[0].innerHTML == blacklist_list[j] ){
                            myTable.rows[i].style.display = "none";
                        }
                    }
                }
            }
        }else {
            for(var i = 0; i < myTable.rows.length; i++) {
                for(var j = 0; j < blacklist_list.length; j++){
                    if(myTable.rows[i].cells[0].innerHTML == blacklist_list[j] ){
                        myTable.rows[i].style.display = "none";
                    }else{
                        myTable.rows[i].style.display = "";
                    }
                }
            }
        }
    }
}



var blacklist_list = []

