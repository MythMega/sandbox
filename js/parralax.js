document.addEventListener("mousemove" , parallax);
function parallax(e){
	this.querySelectorAll('.layer').forEach(layer => {
		const speed = layer.getAttribute('data-speed')
		const x = (window.innerWidth - e.pageX*speed)/20
		const y = (window.innerHeight - e.pageY*speed)/20
		layer.style.transform = `translateX(${x}px) translateY(${y}px)`})}
/*
To use this, you need to have layer like this :
<img src="layer_parralax.png" data-speed="1" class="layer">
data-speed must be between -20 & 20. Negatives values will
make the layer move inverted to mouse movement.

all layer must be in a section with theses css attributes :
<<
    position: relative;
    width: 100%;
    height: 100vh;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
							>>
								
all layer in this section must be with theses css attributes :
<<
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
						>>
*/