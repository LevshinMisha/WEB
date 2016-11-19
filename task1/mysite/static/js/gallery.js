IMAGE_COUNT = 19;

function closeBigImage()
{
    setCookie('img', '-1');
}

document.body.onkeydown = function (e)
{
    if (e.keyCode === 112)
        if (getHelpElement().style.display === 'none')
            showHelp();
        else
            hideHelp();
    if (e.keyCode === 27)
    {
        closeBigImage();
    }
    if (e.keyCode === 37)
    {
        var c = parseInt(getCookie('img')) - 1
        if (c === -1)
            c = IMAGE_COUNT;
        setCookie('img', c.toString());
    }
    if (e.keyCode === 39)
    {
        var c = parseInt(getCookie('img')) + 1
        if (c === IMAGE_COUNT + 1)
            c = 0;
        setCookie('img', c.toString());
    }
}

function expandImage(id)
{
    document.cookie = 'img=' + id + '; path=/;';
    var src_parts = document.getElementById(id).src.split('/');
    var src = '';
    for (var i = 0; i < src_parts.length; i++)
    {
        if (src_parts[i] !== 'thumbnails')
            {
                if (i !== src_parts.length - 1)
                    src += src_parts[i] + '/';
                else
                    src += src_parts[i].slice(0, -7) + '.jpg';
            }

    }
    document.getElementById('gallery_big_img_container').style.display = 'flex';
    document.getElementById('gallery_big_img').src = src;
    document.getElementById('button_make_img_background').onclick = makeBackgroundImage(src);
}



function imgOnClick(id)
{
    setCookie('img', id.toString());
}

function makeBackgroundImage(url)
{
    return function (event)
    {
        setCookie('big_img', url);
    }
}