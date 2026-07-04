import { useEffect, useState } from "react";

import UrlTable from "./components/UrlTable";
import api from "./services/api";
import AddUrlForm from "./components/AddUrlForm";

const POLLING_INTERVAL = 30000;

function App() {

    const [urls, setUrls] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {

      fetchUrls(true);

      const interval = setInterval(() => {

          fetchUrls();

      }, POLLING_INTERVAL);

      return () => clearInterval(interval);

    }, []);

    async function fetchUrls(showLoading = false) {

      try {

          if (showLoading) {
            setLoading(true);
          }

          const response = await api.get("/urls");
          console.log("response.data =", response.data);
          console.log("Is Array?", Array.isArray(response.data));

          setUrls(response.data);

      } catch (error) {

          console.error(error);

      } finally {

          if (showLoading) {
            setLoading(false);
          }

      }
    }

    return (

       <div className="container">

        <h1>Uptime Monitor</h1>

        <AddUrlForm onUrlAdded={fetchUrls} />

        <br />

        {loading
            ? <p>Loading...</p>
            : <UrlTable urls={urls} />
        }

      </div>

    );

}

export default App;