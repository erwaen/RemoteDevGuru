const endpoint = `http://localhost:8001/api/auth/signup`;
const response = await fetch(endpoint, {
    method: "POST",
    headers: {
      "Content-Type": `application/json`,

    },
    body: JSON.stringify({
      username:"marcos",
      password:"12345",
    }),
  });

  const data = await response.json();
  console.log(data);