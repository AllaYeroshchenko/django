
let edu_box_global=document.getElementById('education').innerHTML;
let exp_box_global=document.getElementById('experience').innerHTML;
edu_box_global.id="education_added";
exp_box_global.id="experience_added";
let	btn_edu=document.getElementById('edu');
let	btn_exp=document.getElementById('exp');



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

btn_exp.addEventListener('click', function(){
	let form_for_resume=document.getElementById('add_new_resume');
	exp_box=document.createElement('div');
	exp_box.innerHTML=exp_box_global;
	form_for_resume.insertBefore(exp_box, btn_exp);

})