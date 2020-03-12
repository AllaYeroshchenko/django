
let edu_box_global=document.getElementById('education').innerHTML;
edu_box_global.id="education_added";
let	btn_edu=document.getElementById('edu');
//	form_for_resume=document.getElementById('add_new_resume');
    

btn_edu.addEventListener('click', function(){
	//quant=document.getElementsByClassName('education')
	//console.log(quant)
	//console.log(quant.length+1)
	//edu_box.id='education'+(quant.length+1)
	let form_for_resume=document.getElementById('add_new_resume');
	//let edu_box=edu_box_global.cloneNode(true);
	edu_box=document.createElement('div');
	edu_box.innerHTML=edu_box_global;
	form_for_resume.insertBefore(edu_box, btn_edu);


})