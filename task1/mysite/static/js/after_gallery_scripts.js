document.getElementById('gallery').style.display = 'none';
load_img = new Image();
load_img.onload = function()
    {
        document.getElementById('gallery').style.display = 'block';
        load_img.style.width = "0";
        load_img.style.height = "0";
        document.getElementById('gallery_cash').appendChild(load_img);
    };
load_img.src = "/static/files/loading.gif";