function read_more(){
    var contents = document.getElementsByClassName("article-content");
    for (var i = 0; i < contents.length; i++) {
        content_text = contents.item(i).innerHTML;
        if (content_text.length >= 1000) {
            try {
                contents.item(i).textContent = '';
                var visible_text = content_text.slice(0, 1000);
                var hidden_text = content_text.slice(1001, content_text.length-1);
                var visible_span = document.createElement("span");
                visible_span.innerHTML = visible_text;
                var hidden_span = document.createElement("span");
                hidden_span.innerHTML = hidden_text;
                hidden_span.style.display = "none";
                hidden_span.id = "hidden_" + i.toString()
                var read_more_button = document.createElement("button");
                read_more_button.className = "button-link";
                read_more_button.innerHTML = "read more"
                read_more_button.onclick = function(){
                    if (hidden_span.style.display == "none") {
                        hidden_span.style.display = "block"
                        read_more_button.innerHTML = "read less"
                    } else {
                        hidden_span.style.display = "none"
                        read_more_button.innerHTML = "read more"
                    }
                }
                contents.item(i).appendChild(visible_span);
                contents.item(i).appendChild(hidden_span);
                contents.item(i).appendChild(read_more_button);
            }catch (err) {
                alert('error')
                alert(err.message);
            }
        }
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
    json_http.onloadstart = function() {
        var x = document.getElementById("load");
            if (x.style.display === "none") {
            x.style.display = "block";
            }
    }
    json_http.onload = function() {
        var x = document.getElementById("load");
            if (x.style.display === "block") {
            x.style.display = "none";
            }
    }
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


function show_who_liked(id, model, url) {
    var json_http = new XMLHttpRequest();
    var mod = document.getElementById(id);
    mod.textContent = '';
    json_http.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            try {
                var myObj = JSON.parse(this.responseText);
                liked_usernames = myObj.liked_usernames;
                var mod_head = document.createElement("div");
                mod_head.className = 'modal-header';
                mod_head.innerHTML = "<h4 class='modal-title'>People who liked this</h4><button type='button' class='close' data-dismiss='modal'>&times;</button>";
                mod.appendChild(mod_head);
                usernames = liked_usernames.split('|||');
                for (var c in usernames) {
                    var mod_body = document.createElement("div");
                    mod_body.className = 'modal-body';
                    mod_body.innerText = usernames[c];
                    mod.appendChild(mod_body);
                }
            }
            catch(err) {
                alert(err.message);
            }
        }
    };
    json_http.open("GET", url , true);
    json_http.send();
}
