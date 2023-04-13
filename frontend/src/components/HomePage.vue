<template>
  <b-navbar type="dark" variant="light">
        <b-navbar-brand href="#">World of Lifting</b-navbar-brand>
        <b-button variant="outline-dark" @click="minimizeForm">{{formDisplayText}}</b-button>
  </b-navbar>
  <PowerliftingForm @analyzeLiftsData="onFormSubmit" v-if="shouldDisplayForm"/>
  <PowerliftingResults :liftData="liftData" v-if="shouldLoadResults"/>
</template>

<script>
import PowerliftingForm from './PowerliftingForm.vue';
import PowerliftingResults from './PowerliftingResults.vue';

export default {
  name: 'HomePage',
  components: {
    PowerliftingForm,
    PowerliftingResults,
  },
  data() {
    return {
      shouldLoadResults: false,
      shouldDisplayForm: true,
      formDisplayText: 'Minimize Form',
      liftData: {},
    };
  },
  methods: {
    onFormSubmit(data) {
      // This is where you will update everything with emitted data
      this.liftData = data;
      this.shouldLoadResults = true;
    },
    // Minimizing works visually but the values input by user are lost. TODO save and display values even on minimize
    minimizeForm() {
      this.shouldDisplayForm = !this.shouldDisplayForm;
      if (this.formDisplayText === 'Minimize Form') {
        this.formDisplayText = 'Display Form';
      } else {
        this.formDisplayText = 'Minimize Form';
      }
    },
  },
};
</script>
