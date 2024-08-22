import React from "react";
import {
  ApolloClient,
  InMemoryCache,
  ApolloProvider,
  gql,
  useQuery,
} from "@apollo/client";
import { Text, StyleSheet, View } from "react-native";
import { StatusBar } from "expo-status-bar";

const client = new ApolloClient({
  uri: "http://127.0.0.1:5000/graphql",
  cache: new InMemoryCache(),
});

const HELLO_QUERY = gql`
  query GetHello {
    hello
  }
`;

const Hello = () => {
  const { loading, error, data } = useQuery(HELLO_QUERY);

  if (loading) return <Text>Loading...</Text>;
  if (error) return <Text>Error :(</Text>;

  return (
    <View style={styles.container}>
      <Text>{data.hello}</Text>
    </View>
  );
};

export default function App() {
  return (
    <ApolloProvider client={client}>
      <Hello />
      <StatusBar style="auto" />
    </ApolloProvider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
});
