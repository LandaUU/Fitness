import PropTypes from "prop-types";

import { Accordion, AccordionItem } from "@carbon/react";
import Title from "./Title";
import FoodDiaryAccordionItem from "./Item";

const FoodDiaryAccordion = ({ food, mealName }) => {
  console.log(food);
  return (
    <Accordion className={"food-diary-accordion"}>
      <AccordionItem title={<Title mealName={mealName} food={food} />}>
        {food.map((element) => {
          return <FoodDiaryAccordionItem key={element.id} foodItem={element} />;
        })}
      </AccordionItem>
    </Accordion>
  );
};

FoodDiaryAccordion.propTypes = {
  food: PropTypes.object,
  mealName: PropTypes.string,
};

export default FoodDiaryAccordion;
