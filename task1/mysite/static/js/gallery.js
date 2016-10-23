IMAGE_COUNT = 19;

function closeBigImage()
{
    document.cookie = 'img=-1';
    cookieChange();
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
        document.cookie = 'img=' + c.toString();
        cookieChange();
    }
    if (e.keyCode === 39)
    {
        var c = parseInt(getCookie('img')) + 1
        if (c === IMAGE_COUNT + 1)
            c = 0;
        document.cookie = 'img=' + c.toString();
        cookieChange();
    }
}

function expandImage(id)
{
    document.cookie = 'img=' + id;
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
    document.getElementById('gallery_big_img').src = src;
}

function cookieChange()
{
    if (document.getElementById('gallery') !== undefined)
    {
        if (getCookie('img') === '-1' || getCookie('img') === undefined)
        {
            document.getElementById('gallery_big_img_container').style.display = 'none';
        }
        else
        {
            expandImage(getCookie('img'));
            document.getElementById('gallery_big_img_container').style.display = 'block';
        }
    }
}

function imgOnClick(id)
{
    document.cookie = 'img=' + id;
    cookieChange();
}

