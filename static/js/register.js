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
            nickname: {
                 validators: {
                    notEmpty: {
                         message: '昵称不能为空'
                     },
                    //threshold: 1,
                     remote: {
                      url: "/user/nicknameAjax",
                      data: function (validator) {
                        return {
                          nickname: $("#nickname").val(),
                        };
                      },
                      message: '该昵称已被使用，请使用其他昵称',
                      delay:2000
                    }
                 }
             },

             email: {
                 validators: {
                    notEmpty: {
                         message: '邮箱不能为空'
                     },
                     emailAddress: {
                         message: '邮箱格式不正确'
                     },
                     //threshold: 1,
                      remote: {
                      url: "/user/emailAjax",
                      data: function (validator) {
                        return {
                          email: $("#email").val(),
                        };
                      },
                      message: '该邮箱已被使用，请使用其他邮箱',
                      delay:2000
                    }
                 }
             },
             password: {
                validators: {
                     notEmpty: {
                         message: '密码不能为空'
                     },
                     stringLength: {
                      /*长度提示*/
                      min: 8,
                      max: 30,
                      message: '密码长度必须在8到30之间'
                    },
                      identical: {
                         field: 'confirmPassword',
                         message: '两次密码不一致'
                     },
                     different: {
                         field: 'email',
                         message: '密码不能和邮箱相同'
                     }
                 }
             },
              confirmPassword: {
                 validators: {
                     notEmpty: {
                         message: '密码不能为空'
                     },
                    stringLength: {
                          /*长度提示*/
                          min: 8,
                          max: 30,
                          message: '密码长度必须在8到30之间'
                    },
                     identical: {
                         field: 'password',
                         message: '两次密码不一致'
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