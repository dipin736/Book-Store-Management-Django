$(document).ready(function () {
    $('.paywithRazorpay').click(function (e) { 
        e.preventDefault();
        var isValid = validateForm();
        var token = $("[name='csrfmiddlewaretoken']").val();
            
        if (!isValid) {
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Alert! All Fields are Mandatory",
                footer: '<a href="#">Why do I have this issue?</a>'
            });
            return;
        }

        $.ajax({
            method: "GET",
            url: "/proceed-to-pay",
            success: function (response) {
                var razorpayId = response.razorpay_key;
                var options = {
                    "key": razorpayId,
                    "amount": response.total_cost * 100,
                    "currency": "INR",
                    "name": "Online Book Store Order",
                    "description": "Thank you for buying from us",
                    "image": "https://api-private.atlassian.com/users/2f53e44a56a080cf94841b1a3196d154/avatar",
                    "handler": function (responseFromRazorpay) {
                        data = {
                            "name": $("#id_name").val(),
                            "email": $("#id_email").val(),
                            "mobile": $("#id_mobile").val(),
                            "address": $("#id_address").val(),
                            "city": $("#id_city").val(),
                            "pincode": $("#id_pincode").val(),
                            "payment_id": responseFromRazorpay.razorpay_payment_id,
                            'csrfmiddlewaretoken': token
                        };
                        
                        $.ajax({
                            method: "POST",
                            url: "/booking/",
                            data: data,
                            success: function (response) {
                                Swal.fire({
                                    icon: "success",
                                    title: "Congratulations!",
                                    text: response.status
                                }).then(function () {
                                    window.location.href = '/display/';
                                });
                            },
                            error: function (error) {
                                console.log("Error:", error);
                                Swal.fire({
                                    icon: "error",
                                    title: "Oops...",
                                    text: "Something went wrong. Please try again later.",
                                    footer: '<a href="#">Why do I have this issue?</a>'
                                });
                            }
                        });
                    },
                    "prefill": {
                        "name": $("#id_name").val(),
                        "email": $("#id_email").val(),
                        "mobile": $("#id_mobile").val(),
                        "address": $("#id_address").val(),
                        "city": $("#id_city").val(),
                        "pincode": $("#id_pincode").val(),
                    },
                    "theme": {
                        "color": "#3399cc"
                    }
                };

                var rzp1 = new Razorpay(options);
                rzp1.open();
            }
        });
    });
});

function validateForm() {
    // Add logic to validate form fields
    var isValid = true;

    // Example: Check if the name field is empty
    var nameValue = $("#id_name").val();
    if (!nameValue.trim()) {
        isValid = false;
    }

    // Add similar checks for other form fields
    
    return isValid;
}




