<template>
  <b-navbar type="dark" variant="light">
        <b-navbar-brand href="#">World of Lifting</b-navbar-brand>
  </b-navbar>
  <PowerliftingHomePage v-if="displayPowerlifting" />
  <StrongmanHomePage v-if="displayStrongman" />
  <b-container class="homeContainer" v-if="displayHome">
    <b-row justify-content-center>
      <b-col>
        <h3>Pick which sport you'd like to see your performance in!</h3>
      </b-col>
    </b-row>

    <br>

    <b-row justify-content-center>
      <b-col cols="1"></b-col>
      <b-col cols="5">
        <p>
          Our powerlifting algorithm will let you know how you stack up
           to the competition in the squat, bench, and deadlift!
        </p>
      </b-col>
      <b-col cols="5">
        <p>
          Our strongman analysis is currently a work in progress.
           Come back later to see it in action!
        </p>
      </b-col>
      <b-col cols="1"></b-col>
    </b-row>

    <br>

    <!-- Row for selecting Powerlifting or Strongman stats -->
    <b-row>
      <b-col cols="1"></b-col>

      <b-col class="homeCol" cols="5">
        <b-img
          class="homeBtn"
          src="@/assets/powerliftingBtn.jpg"
          style="height:100%"
          fluid-grow>
        </b-img>
        <h1 class="imageTextCenter">Powerlifting</h1>
      </b-col>

      <b-col class="homeCol" cols="5">
        <b-img
          class="homeBtn"
          src="@/assets/strongmanBtn.jpg"
          style="height:100%"
          fluid-grow>
        </b-img>
        <h1 class="imageTextCenter">Strongman</h1>
      </b-col>

      <b-col cols="1"></b-col>
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
