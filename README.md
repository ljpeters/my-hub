This hub forms the bridge between Shelly i4 and WiZ light bulbs. The Shelly i4 input controller is a smart switch that can trigger requests to Shelly devices or send a http request to a specified link.
This is what happens when the hub is in place and the smart switch is configured properly:
- The Shelly i4 sends a TCP request to this hub, providing the ip address of the light bulb in the request.
- The hub reads the request and performs a UDP request to the specified ip address containing the required state (on/off)

This hub is a small python service running in a docker container. One may choose to run it using podman. Both podman and my-hub run smoothly on a Raspberry Pi 1 B.
