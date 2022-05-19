document.addEventListener("mousemove" , parallax);
function parallax(e){
	this.querySelectorAll('.layer').forEach(layer => {
		const speed = layer.getAttribute('data-speed')
		const x = (window.innerWidth - e.pageX*speed)/20
		const y = (window.innerHeight - e.pageY*speed)/20
		layer.style.transform = `translateX(${x}px) translateY(${y}px)`})}
/*
To use this, you need to have 


*/