<template>
  <b-navbar type="dark" variant="light">
        <b-navbar-brand href="#">World of Lifting</b-navbar-brand>
  </b-navbar>
  <PowerliftingHomePage v-if="displayPowerlifting" />
  <StrongmanHomePage v-if="displayStrongman" />
  <b-container fluid v-if="displayHome">
    <b-row>
      <b-col class="homeCol">
        <b-img
          class="homeBtn"
          src="@/assets/powerliftingBtn.jpg"
          style="height:100%"
          fluid-grow>
        </b-img>
        <h1 class="imageTextCenter">Powerlifting</h1>
      </b-col>

      <b-col class="homeCol">
        <b-img
          class="homeBtn"
          src="@/assets/strongmanBtn.jpg"
          style="height:100%"
          fluid-grow>
        </b-img>
        <h1 class="imageTextCenter">Strongman</h1>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import PowerliftingHomePage from './PowerliftingHomePage.vue';
import StrongmanHomePage from './StrongmanHomePage.vue';

export default {
  name: 'HomePage',
  components: {
    PowerliftingHomePage,
    StrongmanHomePage,
  },
  methods: {},
  data() {
    return {
      displayPowerlifting: false,
      displayStrongman: false,
      displayHome: true,
    };
  },
};
</script>
