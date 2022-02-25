$(
	start
);

function start() {
	/*Initialise Materialize components*/
    $('.sidenav').sidenav();
     $('.modal').modal();
     $('.datepicker').datepicker({
     	format: "dd mmmm, yyyy",
     	i18n: {done: "Select"}
     });
     $('select').formSelect();
}

