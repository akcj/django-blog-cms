$(document).ready(function() {
     // Generate a simple captcha
     function randomNumber(min, max) {
         return Math.floor(Math.random() * (max - min + 1) + min);
     };
     $('#captchaOperation').html([randomNumber(1, 100), '+', randomNumber(1, 200), '='].join(' '));
 
     $('#defaultForm').bootstrapValidator({
 //        live: 'disabled',
         message: 'This value is not valid',
         feedbackIcons: {
             valid: 'glyphicon glyphicon-ok',
             invalid: 'glyphicon glyphicon-remove',
             validating: 'glyphicon glyphicon-refresh'
         },
         fields: {             
             email: {
                 validators: {
                    notEmpty: {
                         message: '邮箱不能为空'
                     },
                     emailAddress: {
                         message: '邮箱格式不正确'
                     }
                 }
             },
             password: {
                validators: {
                     notEmpty: {
                         message: '密码不能为空'
                     },
                     different: {
                         field: 'email',
                         message: '密码不能和邮箱相同'
                     }
                 }
             },
             captcha: {
                 validators: {
                     callback: {
                         message: '错误',
                         callback: function(value, validator) {
                             var items = $('#captchaOperation').html().split(' '), sum = parseInt(items[0]) + parseInt(items[2]);
                             return value == sum;
                         }
                     }
                 }
             }
         }
     });
 
     // Validate the form manually
     $('#validateBtn').click(function() {
         $('#defaultForm').bootstrapValidator('validate');
     });
 
     $('#resetBtn').click(function() {
         $('#defaultForm').data('bootstrapValidator').resetForm(true);
     });
 }); 