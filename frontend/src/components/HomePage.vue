<template>
  <b-navbar type="dark" id="liftingNav">
        <b-navbar-brand href="#">World of Lifting</b-navbar-brand>
  </b-navbar>
  <PowerliftingHomePage v-if="displayPowerlifting" />
  <StrongmanHomePage v-if="displayStrongman" />
  <b-container fluid class="homeContainer" v-if="displayHome">

    <!-- Powerlifting -->
    <b-row align-v="center" class="powerliftingRow homeRow">

      <b-col cols=1></b-col>

      <b-col cols=2>
        <span class="homeTitle">Powerlifting</span>
        <br>
        <span class="homeDesc">Discover how you stack up compared to thousands of lifters!</span>
        <br>
        <span>&#8594;</span>
      </b-col>

      <b-col cols=5></b-col>

      <b-col cols=4>
        <b-img fluid-grow src="@/assets/benchPress/benchPressTransparent.png"></b-img>
      </b-col>

    </b-row>

    <!-- Strongman -->
    <b-row align-v="center" class="strongmanRow homeRow">

      <b-col cols=4>
        <b-img fluid-grow src="@/assets/atlasStones/atlasStonesTransparent.png"></b-img>
      </b-col>

      <b-col cols=5></b-col>

      <b-col cols=2>
        <span class="homeTitle">Odd Lifts</span>
        <br>
        <span class="homeDesc">See how your results rank up next to the competition!</span>
        <br>
        <span>&#8592;</span>
      </b-col>

      <b-col cols=1></b-col>

    </b-row>

    <!-- Running -->
    <b-row align-v="center" class="runningRow homeRow">

      <b-col cols=1></b-col>

      <b-col cols=2>
        <span class="homeTitle">Running</span>
        <br>
        <span class="homeDesc">Explore what level your running is at!</span>
        <br>
        <span>&#8594;</span>
      </b-col>

      <b-col cols=5></b-col>

      <b-col cols=4>
        <b-img fluid-grow src="@/assets/running/runningTransparent.png"></b-img>
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
