<template>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
}

body {
  height: 100%;
}

html {
  height: 100%;
}

.container-fluid {
  height: 100%;
}

.imageTextCenter {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-weight: 900;
  font-size: 36pt;
  text-shadow: 0px 4px 3px rgba(0,0,0,0.4),
             0px 8px 13px rgba(0,0,0,0.1),
             0px 18px 23px rgba(0,0,0,0.1);
}

.row {
  height: 100%;
}

.homeCol {
  position: relative;
  height: 100%;
}

.homeBtn {
  height: 100%;
  -webkit-filter: sepia(1);
  -webkit-filter: sepia(50%);
  -moz-filter: sepia(50%);
  -ms-filter: sepia(50%);
  -o-filter: sepia(50%);
  filter: sepia(50%);
}

.homeBtn:hover {
  filter: none;
  -webkit-filter: sepia(0);
  -moz-filter: sepia(0);
  -ms-filter: sepia(0);
  -o-filter: sepia(0);
  filter: sepia(0);
}

</style>
