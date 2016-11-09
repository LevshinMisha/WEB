function getCookie(name)
{
  var matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

function galleryCheck()
{
    console.log(document.cookie);
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
    console.log('first');

    var clientWidth = window.innerWidth - 12;
    console.log(clientWidth);
    if (clientWidth < 518)
    {
        clientWidth -= clientWidth % 100;
        if (clientWidth < 300)
            clientWidth = 300;
    }
    else
        clientWidth -= clientWidth % 150;
    console.log(clientWidth);
    if (document.getElementById('gallery'))
        document.getElementById('gallery').style.width = clientWidth.toString() + 'px';
    document.getElementById('menu').style.width = clientWidth.toString() + 'px';
}