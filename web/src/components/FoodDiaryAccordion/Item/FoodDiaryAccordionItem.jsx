const FoodDiaryAccordionItem = ({ foodItem }) => {
  return (
    <div className={"food-diary-acc-item-container"}>
      <div className="food-diary-acc-item-row">{foodItem.food_name}</div>
      <div className="food-diary-acc-item-row">{foodItem.amount} g</div>
      <div className="food-diary-acc-item-row">
        <span className={"food-diary-acc-item-info"}>{foodItem.protein}</span>
        <span className={"food-diary-acc-item-info"}>{foodItem.fat}</span>
        <span className={"food-diary-acc-item-info"}>
          {foodItem.carbohydrate}
        </span>
      </div>
    </div>
  );
};

export default FoodDiaryAccordionItem;
