function move()
{
    var obj = document.getElementById("pic1");
    var deltax, deltay;
    deltax = (obj.offsetLeft + 154) % window.innerWidth
    deltay = (obj.offsetTop + 154) % window.innerHeight
    obj.style.left = deltax + 'px';
    obj.style.top = deltay + 'px';
}