<template>
  <b-navbar type="dark" variant="light">
        <b-navbar-brand href="#">World of Lifting</b-navbar-brand>
  </b-navbar>
  <PowerliftingForm @analyzeLiftsData="onFormSubmit" />
  <PowerliftingResults :liftData="liftData" />
</template>

<script>
import PowerliftingForm from './PowerliftingForm.vue';
import PowerliftingResults from './PowerliftingResults.vue';

export default {
  components: {
    PowerliftingForm,
    PowerliftingResults,
  },
  data() {
    return {
      loaded: false,
      liftData: {},
    };
  },
  methods: {
    onFormSubmit(data) {
      // This is where you will update everything with emitted data
      this.liftData = data;
      console.log(data);
    },
  },
};
</script>
