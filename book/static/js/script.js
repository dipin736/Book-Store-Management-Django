  $(document).ready(function(){
    $(".increment-btn").click(function(){
        var quantityInput = $(this).closest('.book_qty').find(".quantity-input");
        var currentValue = parseInt(quantityInput.val());
        quantityInput.val(currentValue + 1);
    });

    $(".decrement-btn").click(function(){
        var quantityInput = $(this).closest('.book_qty').find(".quantity-input");
        var currentValue = parseInt(quantityInput.val());
        if(currentValue > 1){
            quantityInput.val(currentValue - 1);
        }
    });

    $('.add-to-cart-btn').click(function (e){
        e.preventDefault();

        var book_id = $(this).closest('.book_qty').find(".book_id").val();
        var book_qty = $(this).closest('.book_qty').find(".quantity-input").val();
        var token=$('input[name=csrfmiddlewaretoken]').val();
        console.log("Book ID:", book_id);
        console.log("Quantity:", book_qty);

        $.ajax({
            method: "POST",
            url: "/add-to-cart",
            data: {
                'book_id': book_id,
                'book_qty': book_qty,
                csrfmiddlewaretoken: token
            },
            dataType: "json",  // This ensures that jQuery parses the response as JSON
            success: function(response) {
                      // Check the response status and display a pop-up message accordingly
                      alertify.success(response.status);
                      $('.cart-item-count').text(response.cart_item_count);
            },
            error: function(error) {
                // Handle errors here
                console.error(error);
                alertify.error('Error occurred. Please try again later.');
            }
        });

    })

    $('.add-to-wishlist').click(function (e) {
    e.preventDefault();

    var book_id = $(this).closest('.book_qty').find(".book_id").val();
    var token = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
        method: "POST",
        url: "/add-to-wishlist",
        data: {
            'book_id': book_id,
            csrfmiddlewaretoken: token
        },
        dataType: "json",
        success: function(response) {
            alertify.success(response.status);
            $('.wish_item_count').text(response.wish_item_count);
        },
        error: function(error) {
            console.error(error);
            alertify.error('Error occurred. Please try again later.');
        }
    });
});

    $('.delete-cart-item-btn').click(function(e) {
        e.preventDefault();
        var cartItemId = $(this).data('cart-item-id');
        var book_id = $(this).closest('.book_qty').find(".book_id").val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        
        $.ajax({
            method: 'POST',
            url: '/delete-from-cart/' + cartItemId + '/',
            data: {
                'book_id': book_id,
                'csrfmiddlewaretoken': token
            },
            success: function(response) {
                if (response.status === 'success') {
                    alertify.success('Cart item deleted successfully');
                    
                    // Refresh the cart data by reloading the specific element
                    $('.cartdata').load(location.href + " .cartdata", function() {
                        // Additional logic after cart data is refreshed, if needed
                    });
                } else {
                    alertify.error('Error deleting cart item');
                }
            },
            error: function(error) {
                console.error('AJAX error:', error);
                alertify.error('Error occurred. Please try again later.');
            }
        });
    });

    $('.delete-wish-item-btn').click(function(e) {
        e.preventDefault();
        var wishItemId = $(this).data('wish-item-id');
        var book_id = $(this).closest('.book_qty').find(".book_id").val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        
        $.ajax({
            method: 'POST',
            url: '/delete-from-wishlist/' + wishItemId + '/',
            data: {
                'book_id': book_id,
                'csrfmiddlewaretoken': token
            },
            success: function(response) {
                if (response.status === 'success') {
                    alertify.success('Wish item deleted successfully');
                    
                    // Refresh the cart data by reloading the specific element
                    $('.wishdata').load(location.href + " .wishdata", function() {
                        // Additional logic after cart data is refreshed, if needed
                    });
                } else {
                    alertify.error('Error deleting wish item');
                }
            },
            error: function(error) {
                console.error('AJAX error:', error);
                alertify.error('Error occurred. Please try again later.');
            }
        });
    });

    $('.changeQuantity').click(function(e) {
        e.preventDefault();

        var bookQtyInput = $(this).siblings('.quantity-input');
        var bookId = bookQtyInput.closest('.book_qty').find('.book_id').val();
        var bookQty = bookQtyInput.val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: 'POST',
            url: '/update-cart',  // Update the URL to match your Django view URL
            data: {
                'book_id': bookId,
                'book_qty': bookQty,
                'csrfmiddlewaretoken': token
            },
            dataType: 'json',
            success: function(response) {
                // Check the response status and display a message accordingly
                if (response.status === 'Updated successfully') {
                    alertify.success(response.status);
                } else {
                    alertify.error('Failed to update quantity');
                }
            },
            error: function(error) {
                // Handle errors here
                console.error(error);
            }
        });
    });
    
});
