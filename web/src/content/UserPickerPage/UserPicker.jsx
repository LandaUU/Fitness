import { useEffect, useState } from "react";
import { Button, ComboBox, Layer } from "@carbon/react";

const UserPickerPage = () => {
  const [user, setUser] = useState(null);
  const [users, setUsers] = useState(null);

  const fetchUsers = async () => {
    const result = await fetch("http://localhost:8000/users/get", {
      method: "GET",
    });
    return await result.json();
  };

  useEffect(() => {
    console.log(window.Telegram);
    fetchUsers().then((result) => {
      setUsers(result);
      window.Telegram.WebApp.ready();
    });
  }, []);

  return (
    <Layer className="user-picker-container">
      <div className="user-picker-subcontainer">
        <ComboBox
          id="user-picker-box"
          items={users}
          itemToElement={(item) =>
            item ? <span className="user-picker-item">{item.name}</span> : ""
          }
          className="user-picker-box"
          label="Select an option..."
          onChange={(item) => setUser(item.selectedItem)}
          selectedItem={user}
          itemToString={(item) => (item ? item.name : "")}
        />
      </div>
      <div className="user-picker-subcontainer">
        <Button
          className="user-picker-submit"
          onClick={() => {
            window.Telegram.WebApp.sendData(JSON.stringify(user));
          }}
        >
          Выбрать
        </Button>
      </div>
    </Layer>
  );
};

export default UserPickerPage;
