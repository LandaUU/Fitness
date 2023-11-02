import { useEffect, useState } from "react";
import { Button, ComboBox, Layer } from "@carbon/react";

const UserPickerPage = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    window.Telegram.WebApp.ready();
    console.log(`initData = ${window.Telegram.WebApp.initData}`);
  }, []);

  return (
    <Layer className="user-picker-container">
      <div className="user-picker-subcontainer">
        <ComboBox
          items={[
            { id: "1", text: "Иванов Иван Иванович" },
            { id: "2", text: "Сергеев Сергей Сергеевич" },
            { id: "3", text: "Утюгов Виктор Петрович" },
          ]}
          itemToElement={(item) =>
            item ? <span className="user-picker-item">{item.text}</span> : ""
          }
          className="user-picker-box"
          label="Select an option..."
          onChange={(item) => setUser(item.selectedItem)}
          selectedItem={user}
          itemToString={(item) => (item ? item.text : "")}
        />
      </div>
      <div className="user-picker-subcontainer">
        <Button
          className="user-picker-submit"
          onClick={() => {
            window.Telegram.WebApp.sendData(user);
          }}
        >
          Выбрать
        </Button>
      </div>
    </Layer>
  );
};

export default UserPickerPage;
