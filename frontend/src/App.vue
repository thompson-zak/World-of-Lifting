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
  background-color: white;
}

html {
  height: 100%;
}

.homeContainer {
  background-color: white;
}

.homeRow {
  padding-top: 3%;
  padding-bottom: 3%;
  padding-right: 5%;
  padding-left: 5%;
}

.homeTitle {
  font-weight: 700;
  font-size: 3em;
}

.powerliftingRow {
  background-color: orange;
}

.strongmanRow {
  background-color: yellow;
}

.homeRow:hover {
  -webkit-filter: sepia(1);
  -webkit-filter: sepia(50%);
  -moz-filter: sepia(50%);
  -ms-filter: sepia(50%);
  -o-filter: sepia(50%);
  filter: sepia(50%);
}

</style>
