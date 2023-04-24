<template>
  <h2>Powerlifting Analysis</h2>

  <br>

  <b-container>
    <b-row align-h="center">
      <b-col cols=4></b-col>

      <b-col cols=4>

        <FormKit type="form" @submit="onSubmit" :actions="false" name="formTop">
          <FormKit type="multi-step" tab-style="progress" name="formMultiStep">
            <FormKit type="step" name="lifts">
              <FormKit
                  name="squat"
                  type="number"
                  label="Squat"
                  validation="required"
              />
              <FormKit
                name="bench"
                type="number"
                label="Bench"
                validation="required"
              />
              <FormKit
                name="deadlift"
                type="number"
                label="Deadlift"
                validation="required"
              />
              <FormKit
                name="liftUnits"
                type="radio"
                label="Units"
                :options="['lbs', 'kg']"
                value="lbs"
                validation="required"
              />
            </FormKit>

            <FormKit type="step" name="liftClass">
              <FormKit
                  name="equipped"
                  type="radio"
                  label="Equipped?"
                  :options="['Raw', 'Equipped']"
                  value="Raw"
                  validation="required"
              />
              <FormKit
                name="bodyweight"
                type="number"
                label="Bodyweight"
                validation="required"
              />
              <FormKit
                name="bodyweightUnits"
                type="radio"
                label="Units"
                :options="['lbs', 'kg']"
                value="lbs"
                validation="required"
              />
            </FormKit>

            <FormKit type="step" name="demographics">
              <FormKit
                  name="age"
                  type="number"
                  label="Age"
                  validation="required"
              />
              <FormKit
                name="gender"
                type="radio"
                label="Gender"
                :options="['Male', 'Female', 'Non-Binary']"
                value="Male"
                validation="required"
              />

              <!-- using step slot for submit button-->
              <template #stepNext>
                <FormKit type="submit" />
              </template>
            </FormKit>
          </FormKit>
        </FormKit>
      </b-col>

      <b-col cols=4></b-col>
    </b-row>
  </b-container>
</template>

<style>
  .formkit-steps {
    background-color: white;
  }
  /* Radio button styling */
  li.formkit-option {
    display: inline-block;
    margin-right: 5px !important;
    margin-left: 5px !important;
  }
</style>

<script>
import axios from 'axios';

export default {
  name: 'PowerliftingForm',
  emits: ['requestSubmitted', 'analyzeLiftsData'],
  data() {
    return {};
  },
  methods: {
    onSubmit(formData) {
      this.$emit('requestSubmitted', true);

      const path = 'http://backend:5000/analyze-lifts';
      const equippedBool = formData.formMultiStep.liftClass.equipped === 'Equipped';
      const formGender = formData.formMultiStep.demographics.gender;
      let gender = 'M';
      if (formGender === 'Female') {
        gender = 'F';
      }
      if (formGender === 'Non-Binary') {
        gender = 'Mx';
      }
      const requestBody = {
        squat: Number(formData.formMultiStep.lifts.squat),
        bench: Number(formData.formMultiStep.lifts.bench),
        deadlift: Number(formData.formMultiStep.lifts.deadlift),
        liftUnits: formData.formMultiStep.lifts.liftUnits,
        age: Number(formData.formMultiStep.demographics.age),
        bodyweight: Number(formData.formMultiStep.liftClass.bodyweight),
        bodyweightUnits: formData.formMultiStep.liftClass.bodyweightUnits,
        sex: gender,
        equipped: equippedBool,
      };

      axios.post(path, requestBody)
        .then((res) => {
          this.$emit('analyzeLiftsData', res.data);
        })
        .catch((error) => {
          // eslint-disable-next-line
          // TODO - update error handling
          console.error(error);
        });
    },
  },
};
</script>
