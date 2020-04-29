function delete_notification(html_id, url) {
    var json_http = new XMLHttpRequest();
    json_http.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            try {
                var myObj = JSON.parse(this.responseText);
                if(myObj.success == 'success') {
                    var element = document.getElementById(html_id);
                    element.parentNode.removeChild(element);
                    document.getElementById('notification').click();
                };
            }
            catch(err) {
                alert(err.message);
            };
        };
    };
    json_http.open("GET", url , true);
    json_http.send();
}