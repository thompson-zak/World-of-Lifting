<template>
  <b-container fluid class="homeContainer">

    <!-- Powerlifting -->
    <b-row align-v="center" class="powerliftingRow homeRow" v-on:click="onPowerliftingSelect">

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
    <b-row align-v="center" class="strongmanRow homeRow" v-on:click="onOddLiftSelect">

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
    <b-row align-v="center" class="runningRow homeRow" v-on:click="onRunningSelect">

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
export default {
  name: 'HomePage',
  methods: {
    onPowerliftingSelect() {
      this.$router.push({ path: '/powerlifting' });
    },
    onOddLiftSelect() {
      alert('The odd lifts section is curently a WIP. Please come back later!');
    },
    onRunningSelect() {
      alert('The running section is curently a WIP. Please come back later!');
    },
  },
  data() {},
};
</script>
