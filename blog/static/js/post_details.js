function fit_comment_text_area() {
    var isFirefox = typeof InstallTrigger !== 'undefined';
    var isIE = /*@cc_on!@*/false || !!document.documentMode;
    if (isFirefox || isIE) {
      document.getElementById("comment-text").cols = 73;
    }
}


function show_form(id1,id2) {
  var x = document.getElementById(id1);
  if (x.style.display === "none") {
    x.style.display = "block";
  }
  var y = document.getElementById(id2);
  if (y.style.display === "block") {
    y.style.display = "none";
  }
}


function update_like(id, like, pk, url) {
    var json_http = new XMLHttpRequest();
    json_http.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            try {
                var myObj = JSON.parse(this.responseText);
            }
            catch(err) {
                alert(err.message);
            }
            if (myObj.likes == 0) {
                document.getElementById(id).innerHTML = '';
            } else {
                document.getElementById(id).innerHTML = myObj.likes;
            }
            var button_id;
            if (url.toString().includes("child")) {
                button_id = 'child_comment_button_' + pk;
            } else if (url.toString().includes("post")) {
                button_id = 'post_button_' + pk;
            } else {
                button_id = 'comment_button_' + pk;
            }
            if (myObj.mute == 1) {
                document.getElementById(button_id).className = 'btn-sm btn-link border';
            } else {
                document.getElementById(button_id).className = 'btn-sm btn-primary';
            }
        }
    };
    json_http.open("GET", url + '?like=' + like.toString() + '&pk=' + pk.toString() , true);
    json_http.send();
}