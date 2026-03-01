// ==========================
// MODAL CONTROL
// ==========================

// Add Modal
function showAddForm() {
    document.getElementById("addModal").style.display = "flex";
}

function closeAddForm() {
    document.getElementById("addModal").style.display = "none";
}

// Update Modal
function openUpdateModal(id, name, type, price, quantity) {
    document.getElementById("updateModal").style.display = "flex";

    document.getElementById("updateId").value = id;
    document.getElementById("updateName").value = name;
    document.getElementById("updateType").value = type;
    document.getElementById("updatePrice").value = price;
    document.getElementById("updateQuantity").value = quantity;
}

function closeUpdateForm() {
    document.getElementById("updateModal").style.display = "none";
}


// ==========================
// DROPDOWN CONTROL
// ==========================

document.addEventListener("DOMContentLoaded", function () {
    const dropdownBtn = document.getElementById("allProductsBtn");
    const dropdownMenu = document.getElementById("dropdownMenu");

    dropdownBtn.addEventListener("click", function () {
        dropdownMenu.style.display =
            dropdownMenu.style.display === "block" ? "none" : "block";
    });
});


// ==========================
// SEARCH FUNCTIONS
// ==========================

function showFindById() {
    const container = document.getElementById("searchContainer");
    container.style.display = "block";
    document.getElementById("searchInput").placeholder = "Enter Product ID";
}

function showFindByType() {
    const container = document.getElementById("searchContainer");
    container.style.display = "block";
    document.getElementById("searchInput").placeholder = "Enter Product Type";
}

function clearSearch() {
    document.getElementById("searchInput").value = "";
    document.getElementById("searchContainer").style.display = "none";
}


// ==========================
// FORM HANDLERS (Optional)
// ==========================

function handleSearch(event) {
    event.preventDefault();
    const value = document.getElementById("searchInput").value;
    console.log("Searching for:", value);
}

function handleAddProduct(event) {
    event.preventDefault();
    console.log("Add Product submitted");
}

function handleUpdateProduct(event) {
    event.preventDefault();
    console.log("Update Product submitted");
}