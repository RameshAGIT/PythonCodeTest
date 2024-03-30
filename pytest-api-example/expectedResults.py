EXPECTED_RESULTS = {
    "order_not_found": {
        "message": "Order not found"
    },
    "successful_order": {
        "message": "Order and pet status updated successfully"
    },
    "get_pet": {
        "message": "Success"
    },
    "status_codes": {
        "success": 200,
        "not_found": 404
    },
    "endpoint": {
        "get_pet_by_id": "/pets/1",
        "get_pet_by_id_404": "/pets/10",
        "get_pet_by_status": "/pets/findByStatus",
        "patch_store_by_orderId": "/store/order/",
    },

}
