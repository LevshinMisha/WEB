document.getElementById('gallery').style.display = 'none';
load_img = new Image();
load_img.onload = function()
    {
        document.getElementById('gallery_cash').appendChild(load_img);
        document.getElementById('gallery').style.display = 'block';
    };
load_img.src = "/static/files/loading.gif";