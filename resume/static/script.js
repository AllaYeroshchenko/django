//let edu_box_global_it=document.getElementById('education_hidden');


let edu_box_global=document.getElementById('education').innerHTML;

let exp_box_global=document.getElementById('experience').innerHTML;

edu_box_global.id="education_added";
exp_box_global.id="experience_added";
let edu_max_number=document.getElementsByClassName('education').length;
let exp_max_number=document.getElementsByClassName('experience').length;


let	btn_edu=document.getElementById('edu');
let	btn_exp=document.getElementById('exp');



btn_edu.addEventListener('click', function(){
	edu_max_number=edu_max_number+1;
	let form_for_resume=document.getElementById('resume_form');
	edu_box=document.createElement('div');
	edu_box.innerHTML=edu_box_global;
	edu_box.id="education"+edu_max_number;
	edu_box.setAttribute("name", "education"+edu_max_number);
	edu_box.setAttribute("class", "education");
	but_del_ed=edu_box.getElementsByClassName('del_edu')[0];
	but_del_ed.id="del_edu"+edu_max_number;
	but_del_ed.name="del_edu"+edu_max_number;
	but_del_ed.setAttribute('onclick', 'delete_education('+edu_max_number+')');
	form_for_resume.insertBefore(edu_box, btn_edu);

})

btn_exp.addEventListener('click', function(){
	exp_max_number=exp_max_number+1;
	let form_for_resume=document.getElementById('resume_form');
	exp_box=document.createElement('div');
	exp_box.innerHTML=exp_box_global;
	exp_box.id="experience"+exp_max_number;
	exp_box.setAttribute("name", "experience"+exp_max_number);
	exp_box.setAttribute("class", "experience");
	but_del_exp=exp_box.getElementsByClassName('del_exp')[0];
	but_del_exp.id="del_exp"+exp_max_number;
	but_del_exp.name="del_exp"+exp_max_number;
	but_del_exp.setAttribute('onclick', 'delete_experience('+exp_max_number+')');
	form_for_resume.insertBefore(exp_box, btn_exp);

})

