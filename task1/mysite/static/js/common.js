function getCookie(name)
{
  var matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

function galleryCheck()
{
    if (document.getElementById('gallery') !== null)
    {
        if (getCookie('img') === '-1' || getCookie('img') === undefined)
        {
            document.getElementById('gallery_big_img_container').style.display = 'none';
        }
        else
        {
            expandImage(getCookie('img'));
        }
    }
}

function bigImgCheck()
{
    if (getCookie('big_img') !== undefined)
    {
        document.body.style.backgroundImage = 'url(' + getCookie('big_img') + ')';
    }
}

function checks()
{
    galleryCheck();
    bigImgCheck();
}

function setCookie(name, value)
{
    document.cookie = name + '=' + value + '; path=/;';
    checks();
}


function getHelpElement()
{
    return document.getElementById('help')
}


function showHelp()
{
    getHelpElement().style.display = 'block';
}

function hideHelp()
{
    getHelpElement().style.display = 'none';
}

window.onload = function (event)
{
    checks();
    var help = document.getElementById('help');
    if (help !== null)
    {
        help.style.display = 'none';
        help.style.whiteSpace = 'pre-wrap';
        help.innerHTML = 'Нажмите F1, чтобы открыть\\закрыть хелп\nНажимайте на миниатюру чтобы увидеть полную картинку\nПеремещение по галерее с помощью стрелок\nESC - закрывает картинку';
    }
    onResize();
}

window.onresize = function(event)
{
    onResize();
};

function onResize()
{
    var clientWidth = window.innerWidth - 25;
    if (clientWidth < 476)
    {
        clientWidth -= clientWidth % 100;
        if (clientWidth < 300)
            clientWidth = 300;
    }
    else
        clientWidth -= clientWidth % 150;
    if (document.getElementById('gallery'))
    {
        document.getElementById('gallery').style.width = clientWidth.toString() + 'px';
        if (clientWidth > 1200)
            document.getElementById('gallery_big_img').style.width = (clientWidth - 600).toString() + 'px';
        else if (clientWidth > 600)
            document.getElementById('gallery_big_img').style.width = (clientWidth - 300).toString() + 'px';
        else
            document.getElementById('gallery_big_img').style.width = (clientWidth).toString() + 'px';
    }
    document.getElementById('header').style.marginLeft = '-'+ ((window.innerWidth - clientWidth) / 2).toString() + 'px';
    document.getElementById('header').style.marginRight = '-'+ ((window.innerWidth - clientWidth) / 2).toString() + 'px';
    document.getElementById('menu').style.width = clientWidth.toString() + 'px';
    document.getElementById('main_content').style.width = (clientWidth).toString() + 'px';
    document.body.style.width = (clientWidth).toString() + 'px';
}