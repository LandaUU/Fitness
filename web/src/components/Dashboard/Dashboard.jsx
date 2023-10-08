import { useLoaderData } from "react-router-dom";
import { Accordion, AccordionItem, Grid, Column } from "@carbon/react";
import { useEffect } from "react";
import { Restaurant } from "@carbon/icons-react";

const Dashboard = () => {
  const food = useLoaderData();

  const meal_names = [...new Set(food.map((element) => element.meal_name))];

  useEffect(() => {}, []);

  return (
    <Grid fullWidth>
      <Column lg={16} md={8} sm={4}>
        <Accordion>
          {meal_names.map((meal) => {
            let my_food = food.filter((f) => f.meal_name == meal);
            return (
              <AccordionItem
                title={
                  <span>
                    <Restaurant />
                    <text>{meal}</text>
                  </span>
                }
                key={meal}
              >
                {my_food.map((element) => {
                  return <div key={element.id}>{element.food_name}</div>;
                })}
              </AccordionItem>
            );
          })}
        </Accordion>
      </Column>
    </Grid>
  );
};

export default Dashboard;
