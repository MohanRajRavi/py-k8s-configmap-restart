from kubernetes import client, config

namespacelist = []


def conn_ns():
    try:
        config.load_kube_config(config_file="C:\\Users\\moravi\\.kube\\config")
        print("connected")
        v1 = client.CoreV1Api()
        ns = v1.list_namespace().items
        for namespace in ns:
            namespacelis = namespacelist.append(namespace.metadata.name)
            # print("name is ", namespace.metadata.name)
        # print("name outside", namespacelist)

        for i in namespacelist:
            print("namespace is ", i)
            pods = v1.list_namespaced_pod(i).items
            for pod in pods:
                print("pods in", i, "is", pod.metadata.name)

        '''commenting the pods stuff
        pod = v1.list_namespaced_pod('default')
        pods = pod.items
        pods_name = [print("new name is",pod.metadata.name) for pod in pods]
        for pod in pods:
            print("pod is", pod.metadata.name)
        '''

    except():
        print("an exception occurred")


if __name__ == '__main__':
    conn_ns()
