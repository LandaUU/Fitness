import PropTypes from "prop-types";

import { Accordion, AccordionItem } from "@carbon/react";

const FoodDiaryAccordeion = ({ food, mealName }) => {
  console.log(food);
  return (
    <Accordion>
      <AccordionItem title={mealName}>
        {food.map((element) => {
          return <div>{element.food_name}</div>;
        })}
      </AccordionItem>
    </Accordion>
  );
};

FoodDiaryAccordeion.propTypes = {
  food: PropTypes.object,
  mealName: PropTypes.string,
};

export default FoodDiaryAccordeion;
