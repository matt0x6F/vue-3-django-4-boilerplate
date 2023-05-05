<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <router-link to="/" class="navbar-brand">Navbar</router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
                <router-link to="/" class="nav-link active" aria-current="page"><span class="material-icons-two-tone">
                home</span>Home</router-link>
                <router-link to="/about" class="nav-link">About</router-link>
                <router-link to="/products" class="nav-link">Products</router-link>
            </div>
            </div>
        </div>
    </nav>
</template>