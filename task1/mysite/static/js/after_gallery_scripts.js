document.getElementById('gallery').style.display = 'none';
load_img = new Image();
load_img.onload = function()
    {
        document.getElementById('gallery').style.display = 'block';
        document.getElementById('gallery_cash').appendChild(load_img);
    };
load_img.src = "/static/files/loading.gif";